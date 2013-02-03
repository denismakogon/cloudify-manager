package org.openspaces.servicegrid.agent.tasks;

import org.openspaces.servicegrid.ImpersonatingTask;
import org.openspaces.servicegrid.agent.state.AgentState;

public class StartMachineTask extends ImpersonatingTask {

	public StartMachineTask() {
		super(AgentState.class);
	}
}
