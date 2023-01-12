# AbstractBaseUser
everything you need to know about Custom Django User Model



AbstractUser
AbstractUser class inherits the User class and is used to add Additional Fields required for your User in Database itself. SO its change the schema of the database. It is basically used to add fields like date_of_birth , location and bio etc. to the existing User model This is Done to the very Beginning of the project. which means you will get the complete field which by default come with the user Model plus the following field that you add/define.




AbstractBaseUser

AbstractBaseUser has the authentication functionality only , it has no actual fields you will supply the fields to use when you subclass.

you have to till that what field represent username fields, and how those users will be managed

for example you have to use email in your authentication , Normally Django use username in authentication, so how do you change it to use email?


Its Time to Decision Now which one should you use ?
If you need full control over User model, it is better to use AbstractBaseUser but if you are just adding things to the existing user, for example, you just want to add an extra field bio ,location field or any other profile data then use AbstractUser.
