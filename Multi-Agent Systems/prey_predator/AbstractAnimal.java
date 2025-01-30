import java.awt.Color;
import java.awt.Graphics2D;

import turtlekit.kernel.Turtle;

public class AbstractAnimal extends Turtle {
		
	private static int nextId = 0;
	protected int id;
	protected int fieldOfVision = 5;
	// potential acceleration
	
	public AbstractAnimal(String initMethod) {
		super(initMethod);
		this.id = nextId++;		
	}
	
	public int getId() {
        return id;
    }
	
//	protected void drawVisionRadiusBorder() {
//        Graphics2D g2d = getGraphics();
//        if (g2d != null) {
//            g2d.setColor(Color.white);
//            g2d.drawOval(x - fieldOfVision, y - fieldOfVision, 2 * fieldOfVision, 2 * fieldOfVision);
//        }
//    }
	
//	@Override
//	protected void activate() {
//		super.activate();
//	}

}
