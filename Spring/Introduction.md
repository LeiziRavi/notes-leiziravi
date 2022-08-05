#### developer:
- Rod Jhonson


#### Organisation:
- __Earlier__: Spring org
- __Now__: Pivotal

#### Initial Name:
- Interface 21
- later changed to Spring (which is a season)


- __WHY NAMES SPRING?__
- Came against EJBs (Enterprise Java Beans)
- While comparing with EJBs, EJBs are like winter season, after winter next season is _SPRING_.

- #### Difference between EJBs and Spring
	- EJBs are heavyweight and tightly coupled
		- EJBs has dependency on app server, where as spring do not have such dependency.
	- Spring applications are lightweight and loosely coupled


- #### Difference between awt and swing
	- awt has dependency of OS libraries, hence heavyweight.
	- swings do not have os library dependency, they are dependent on jdk libraries, hence lightweight.


- In MVC:
	- View
	- Controller
	- Model
		- Business Layer
		- Service Layer
		- DAO
			- Data Access classes can be build using 
				- JDBC api
				- Hibernate
				- JPA
				- Ibatis


#### HOW WE CAN MAKE TWO CLASSES LOSSELY COUPLED?

- If we make instance of a class directly inside another class, it becomes tightly coupled.
- For loose coupling: instead of creating class instance use interface.