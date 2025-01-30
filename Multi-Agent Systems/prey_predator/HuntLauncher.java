import static turtlekit.kernel.TurtleKit.Option.turtles;
import static turtlekit.kernel.TurtleKit.Option.noWrap;
import static turtlekit.kernel.TurtleKit.Option.envHeight;
import static turtlekit.kernel.TurtleKit.Option.envWidth;
import static turtlekit.kernel.TurtleKit.Option.viewers;

import turtlekit.kernel.TKLauncher;
import turtlekit.viewer.PheromoneViewer;
import turtlekit.viewer.PopulationCharter;

public class HuntLauncher extends TKLauncher {
	
// 	private boolean WRAP=true
	
	protected void createSimulationInstance() {
		
		setMadkitProperty(turtles, 
				Prey.class.getName() + "," + 60
				+ ";" +
				Predator.class.getName() + "," + 60
				);
		setMadkitProperty(noWrap, "false");
		setMadkitProperty(envHeight, "200");
		setMadkitProperty(envWidth, "200");
		setMadkitProperty(viewers, 
				PheromoneViewer.class.getName()
				+ ";" +
				PopulationViewer.class.getName());
		
		super.createSimulationInstance();
	}
	
	public static void main(String[] args) {
		executeThisLauncher();
		//System.err.print("Hello World!");
	}
	
	class PopulationViewer extends PopulationCharter{
		public PopulationViewer() {
			setTimeFrame(2000);
		}
	}


}


