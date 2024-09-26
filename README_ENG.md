![обложка]()


 
| Participant | Role | Task |
|----------|------|--------|
| Sherstobitov Oleg Andreevich | Programmer | Drone programming |
| Rzhannikova Elena Andreevna | Programmer | Working with AI |

# The problem and the goal
According to traffic police statistics, in 2023, 33% of accidents occurred due to poor-quality roads. That is, every 3 drivers risks damaging the car due to a pit or pothole. The main reason for the poor condition of the roadway is the late detection and repair of damage. We propose using an autonomous drone to fly over roads, use a neural network to detect pits and transmit information to road services. And with the help of an autonomous rover, repair these pits.

# Job Description
The quadcopter autonomously flies around city streets and uses a neural network to detect pits and defects in the roadway. All data about the defects found is sent to the server, which makes a damage map. At night, when there are fewer cars on the roads, the autonomous rover goes out to repair the road. He moves along a pre-arranged route, observing traffic rules, recognizing traffic lights and so on. Upon arrival at the work site, the rover uses lidar to scan the pit, determine its size and volume. Based on the data received, he decides on self-repair or transfer of information that this pit needs to be eliminated manually. If the pit is suitable for autonomous repair, it feeds the required volume of asphalt concrete mixture into the pit, and then drives through it, leveling it.

# System requirements:
- The quadcopter must be able to fly around city streets autonomously.
- The neural network must process the image from the drone's camera and recognize different pits.
- The server must create a damage map based on the data received from the quadcopter.
- The server must create the optimal route for the rover

# Project objectives
- Prepare a dataset and train a neural network to recognize test card pits.
- Configure the drone to work offline. Download and debug the neural network on the drone.
- To develop an algorithm for working with recognition results: counting the number of pits, determining their coordinates, transmitting data to the server.
- To develop a server application with the function of receiving data from a drone, processing pit data, collecting statistics and transmitting information about detected pits to users.
- Test the system and make changes based on the test results.

[**`Project implementation`**](https://github.com/ElenaRzh/Autonomous-road-surface-monitoring-and-repair-system./blob/main/DEVELOPMENT.md)

[**`Distribution of tasks`**](https://github.com/user-attachments/files/17146064/Tasks.xlsx)

[**`The procedure for performing checks`**](https://github.com/user-attachments/files/17132886/system_test.xlsx)