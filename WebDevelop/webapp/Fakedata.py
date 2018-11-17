from faker import Faker
fake = Faker()
for i in range(20):
    print(fake.name())
    print(fake.email())
    print(fake.address())

"""
StartProject djproject
  StartApp testapp
  templates
    Blorejobs.html
    index.html
    Chennai.html
  static 
    css
      demo.css
    images
      hyd1.jpg
      hyd2.jpg
      hyd3.jpg
    
Add Application Name
    Template path
    Static Path
    Settings.py
    
Models.py
   hydjobs
   blrjobs
makemigrations
migrate

   
    
"""