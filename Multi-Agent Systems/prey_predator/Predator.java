import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

import turtlekit.kernel.Patch;
import turtlekit.kernel.Turtle;
import turtlekit.pheromone.Pheromone;

public class Predator extends AbstractAnimal {
	
	
	 protected boolean MOVE_CONSTRAINED=false;
	 protected boolean STIGMERGY=true;
	 protected boolean PACKS=false;
	 protected int PACK_SIZE = 5;
	
	int EVAPORATION = 25;
	
	private Prey target;
	private Pheromone pheromone;
	private Predator alpha;

	private int steps = 0;
	
	private String[] behaviours = {"alone", "inPack", "dead"};
	private String currentBehaviour;
	
	private List<Predator> pack;
	
	public Predator() {
		super("live");
	}
	
	public String live() {
		playRole("predator");
		// setColor(new Color((int) (Math.random() * 256),(int) (Math.random() * 256), (int) (Math.random() * 256)));
		setColor(Color.red);
		setBehaviour("alone");
		return "look";
	}
	
	public String look() {
		if (PACKS) {
			List<Turtle> predatorsHere = getPatch().getTurtlesWithRole(getFieldOfVision(), true, "predator");
			if (predatorsHere.size() == 1)
				setHeading(predatorsHere.getFirst().getHeading());
			else if (predatorsHere.size() <= PACK_SIZE && predatorsHere.size() >= 2) {
				pack = new ArrayList<>();
				for (Turtle t : predatorsHere) {
					Predator p = (Predator) t;
					pack.add(p);
					setBehaviour("inPack");
		        }
				
				if (pack != null) {
					Predator predatorWithMinID = pack.get(0);
			        for (Predator predator : pack) {
			            if (predator.getId() < predatorWithMinID.getId()) {
			                predatorWithMinID = predator;
			            }
			        }
			        
			        setAlpha(predatorWithMinID);
			        
			        Color minIDColor = predatorWithMinID.getColor();
			        for (Predator predator : pack) {
			            predator.setColor(minIDColor);
			        }
				}
				return "move";
			}
			else
				return "move";		
			}
		
		target = getNearestTurtle(getFieldOfVision(), Prey.class);
		if (target != null) {
			setTarget(target);
			return "hunt";
		} else {
			return "move";
		}	
	}
	
	public String move() {
		if (MOVE_CONSTRAINED) {
			fd(1);
			if (getColor() == Color.green) {
				steps++;
			}
			if (steps % 20 == 0) {
//				System.out.println("Old heading" + getHeading());
				setHeading(getHeading() + 15);
//				System.out.println("walked " + steps + "steps ");
//				System.err.println("New heading" + getHeading() + 20);
			}	
		} 
		
		if (STIGMERGY) {
			if (pheromone != null && getFieldValue(pheromone) > 1500)
				smell("trail");
		}
		
		if (PACKS) {
			if (alpha == this || alpha == null) {
				wiggle();
			} else {
				step();
				setHeadingTowards(alpha);
			}
			return "look";
		}	
		
		// Move without constraints
		wiggle();		
		return "look";
	}
	
	public String hunt() {
		if (STIGMERGY) {
			pheromone = getEnvironment().getPheromone("trail", 5, 5);
			pheromone.incValue(xcor(), ycor(), 5000);
			setColor(Color.red);
		}
		setHeadingTowards(target);
		return "look";
	}
	
	// GETTERS & SETTERS (FOV, ID, ) //
	public int getFieldOfVision(){
		return this.fieldOfVision;
	}
	
	public int getId(){
		return this.id;
	}
	
	
	public void setTarget(Prey target) {
		this.target = target;
	}
	
	public void setBehaviour(String newBehaviour) {
        // Check if the new state is a valid state (is included in our states[] array)
        for (String validBehaviour : behaviours) {
            if (validBehaviour.equals(newBehaviour)) {
            	this.currentBehaviour = newBehaviour;
                return;
            }
        }
        // If the new state is not valid, set to default state ("alone")
        this.currentBehaviour = "alone";
    }

    public String getBehaviour() {
        return this.currentBehaviour;
    }
    
    public void setAlpha(Predator alpha) {
    	this.alpha = alpha;
    }
	
	
	public static void main(String[] args) {
		System.err.print("Hello World!");
	}
}
