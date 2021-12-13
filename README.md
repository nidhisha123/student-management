# student-management
Student Management

JWT Token is used for authentication
api token url - account/api/token/
  params : username, password
refresh token url - account/api/token/refresh/
  params : refresh

Add or list grades
  url : api/grade/
  list :
    method : GET
    extra :
      - search by name
      - cursor pagination
  create :
    method : POST
    params : name

Single object operations
  url : api/grade/<grade_id>/
  methods : GET, PUT, PATCH and DELETE
   
Add or list students
  url : api/student/
  list :
    method : GET
    extra : 
      - search by name, grade__name
      - sort by age
      - pagination limitoffset
  create :
    method : POST
    params : name, age, grade

Single object operations
  url : api/student/<student_id>/
  methods : GET, PUT, PATCH and DELETE
 
User registration
  url : account/register/
  params : username, email, password, password2
