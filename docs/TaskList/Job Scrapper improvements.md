## Job Scrapper improvements <Badge text="Golang" type="warn" /> 
[[toc]] 
### Job Scrapper improvements

#### Reporting

Adding new plots, breaking down technologies, AWS vs Google App Container, vs heroku and other sources

Programming languages I'm confortable with vs unfamilar with.

More charts essentially and data.
#### Back End
Probably deploy to heroku and have two separate apps, one for the front-end and one for the back-end, although I could have heroku on the back-end and firebase for the front-end. Think about it some more, definitely have the app in separate repos.

|Search Time|# Jobs | Avg Keywords | Avg Skills | City | Search Terms | Date |
|---| ---| ---| ---| --- | --- | ---|
|Time| int| number | number | string | string | Date |

Table 1: Schema for postgres database.

https://medium.com/@siobhanpmahoney/deploying-a-react-frontend-rails-backend-project-to-heroku-4b2c4f6f630c



https://flaviocopes.com/golang-tutorial-rest-api/

https://flaviocopes.com/vue-introduction/

Probably get a golang backend. test with insomnia and then write some automatic tests

#### Plan

1. [Building and Testing a REST API in Go with Gorilla Mux and PostgreSQL - Semaphore](https://semaphoreci.com/community/tutorials/building-and-testing-a-rest-api-in-go-with-gorilla-mux-and-postgresql)
2.  [GitHub - tsauvajon/restapi-go-vue: Go REST Api + postgres + Vue frontend boilerplate](https://github.com/tsauvajon/restapi-go-vue), honestly the back end doesn't matter so much? I think you need to have two seperate repos, coul.
3.  Deploy with [Build and Deploy a secure REST API with Go, Postgresql, JWT and GORM](https://medium.com/@adigunhammedolalekan/build-and-deploy-a-secure-rest-api-with-go-postgresql-jwt-and-gorm-6fadf3da505b)
 
 !!! danger Things to be aware of 
 Convential Widsom suggests that I need to have two repos, one for the front-end and one for the back-end.
 !!!
 
 !!! note career maybe build a REST API
 For the UVIC Career Center Job Scrapping, link it to the RESTFUL API in python creating using swagger tools. We will see if that is a good idea.
 
 1. Create rest API that contains "url", and file name ex: `job123645.html` and from the front-end append url such as lopsided-government.surge.sh/job123625.html
 2. Build simple front-end using vue-good-table or equvialent.
!!!

##### OnGoing Tasks

!!! danger Task List
###### Major Tasks
- [x] Modify Go-API for my needs
- [ ] Change search time field from a string to a time 
- [ ] Add more tests to the system
- [x] Configure CI using circle and/or travis, both cause I'm a memer and update ReadMe.md with the badge (actually I think circleCI is better.)

###### Minor Tasks
- [ ] Finish writing unit tests 
- [ ] Deploy to heroku (via travis is ideal)
- [ ] Build client side application 
- [ ] Configure scripts to send data to api
!!!

###### Links
* [Build and Deploy a secure REST API with Go, Postgresql, JWT and GORM](https://medium.com/@adigunhammedolalekan/build-and-deploy-a-secure-rest-api-with-go-postgresql-jwt-and-gorm-6fadf3da505b)
* [Building and Testing a REST API in Go with Gorilla Mux and PostgreSQL - Semaphore](https://semaphoreci.com/community/tutorials/building-and-testing-a-rest-api-in-go-with-gorilla-mux-and-postgresql)
* [Building a RESTful API with Golang | Codementor](https://www.codementor.io/codehakase/building-a-restful-api-with-golang-a6yivzqdo)
* [GitHub - tsauvajon/restapi-go-vue: Go REST Api + postgres + Vue frontend boilerplate](https://github.com/tsauvajon/restapi-go-vue)