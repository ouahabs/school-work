import java.awt.Color;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import turtlekit.kernel.Turtle;


public class Prey extends AbstractAnimal {
	
	
	protected boolean MOVE_CONSTRAINED=true;
	protected boolean STIGMERGY=true;
	// private boolean DIVIDE_AND_CONQUER=true;
	// private boolean PACKS=true;
	// private int final PACK_MAX=5;
	
	private int oldXCor;
	private int oldYCor;
	
	private String[] behaviours = {"flee", "move", "dead"};
    private String currentBehaviour;

    
    // private Timer colorChangeTimer;
    private int cycleCount = 0;
    	
	public Prey() {
		super("live");
 		// System.err.print("My id is: " + getId());
	}
	
	// Live is the activate() function
	// Since 
//	public void activate() {
//		int code = get1DIndex();
////		System.out.println(code);
//		playRole("prey");
//		setColor(Color.white);
//		randomHeading();
//		randomLocation();
//		setNextAction("look");
//	}
	
	public String live() {
//		System.out.println("Living!");
		setColor(Color.white);
		randomHeading();
		randomLocation();
		playRole("prey");
		oldXCor = xcor();
		oldYCor = ycor();
		return "look";
	}
	
	public String look() {
		final Turtle neighborTurtle = getNearestTurtleWithRole(getFieldOfVision(), "prey");
		Prey neighborPrey = (Prey) neighborTurtle;
		if (neighborPrey != null && neighborPrey.getBehaviour() == "flee") {
			setBehaviour("flee");
			return "flee";
		}
		
		final List<Turtle> predatorsHere = getPatch().getTurtlesWithRole(getFieldOfVision(), true, "predator");
		if (!predatorsHere.isEmpty()) {
			if (MOVE_CONSTRAINED) {
				if (oldXCor == xcor() && oldYCor == ycor()) {
					setBehaviour("dead");
					return "dead";
				} else {
					oldXCor = xcor();
					oldYCor = ycor();
				}
			}
			else {
				if (predatorsHere.size() >= 4) {
					setBehaviour("dead");
					return "dead";
				} else {
					setBehaviour("dead");
					return "dead";
				}	
			}
			if (MOVE_CONSTRAINED) {
				setBehaviour("flee");
				return "flee";
			}
		}
		if (predatorsHere.isEmpty()) {
			setBehaviour("move");
			return "move";
		}
		return "look";
	}
	
	public String move() {	
	    if (getBehaviour() == "move") {
	    	if (STIGMERGY) {
	    		if (getColor() == Color.orange) {
	    			cycleCount++;
			    	if (cycleCount % 70 == 0)
			    		setColor(Color.blue);
    				}
	    		// System.out.println(cycleCount);
//	    		return "move";
	    	}
	    	wiggle();
	    	System.out.println(xcor() + "," + ycor());
	    }
		return "look";
	}
	
	public String flee() {
		if (MOVE_CONSTRAINED) {
			if (getBehaviour() == "flee") {
				List<Turtle> toEscapeFrom = new ArrayList<>();
				
				List<Turtle> predatorsHere = getPatch().getTurtlesWithRole(getFieldOfVision(), true, "predator");
				if (!predatorsHere.isEmpty()) {
					setHeading(towards(predatorsHere.getFirst()) + 180);
					for (Turtle turtle : predatorsHere) {
			            toEscapeFrom.add(turtle);
			        }
				}
				
				fd(3);
				
				if (STIGMERGY) {
					setColor(Color.orange);
				}
				
				final Turtle neighborTurtle = getNearestTurtleWithRole(getFieldOfVision(), "prey");
				Prey neighborPrey = (Prey) neighborTurtle;
				if (neighborTurtle != null && neighborPrey.getBehaviour() == "flee") {
					setHeading(towards(neighborTurtle) + 180);
					toEscapeFrom.add(neighborTurtle);
				}
				
				int sum = 0;
				for (Turtle turtle : toEscapeFrom) {
					sum += turtle.getHeading();
		        }
				sum = sum % 360;
				setHeading(getHeading() + sum);
				
			}
		}
		return "look";
	}
	
	@SuppressWarnings("null")
	public String dead() {
		System.err.println("Dead (called)");
		return null;
		
	}
	
	// GETTERS & SETTERS (FOV, ID, ) //
	public int getFieldOfVision(){
		return this.fieldOfVision;
	}
	
	public int getId(){
		return this.id;
	}
	
    public void setBehaviour(String newBehaviour) {
        // Check if the new state is a valid state (is included in our states[] array)
        for (String validBehaviour : behaviours) {
            if (validBehaviour.equals(newBehaviour)) {
            	currentBehaviour = newBehaviour;
                return;
            }
        }
        // If the new state is not valid, set to default state ("move")
        currentBehaviour = "move";
        setNextAction(currentBehaviour);
    }

    public String getBehaviour() {
        return currentBehaviour;
    }
	
//    public void DrawVision() {
//		Turtle turtle = getPatch().getNearestTurtle(getFieldOfVision(), true, Predator.class);
//			
//    }
    
	public static void main(String[] args) {
		System.err.print("Hello World!");
	}
}


