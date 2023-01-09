# Social network only with posts

CRUD for users with posts , opportunity to like another posts on FastAPI framework

For launching app : 

-- clone rep

-- create venv in directory with project:

      python -m venv venv
      
-- activate venv:

      venv/Scripts/activate.ps1
      
-- install requirements.txt:

      pip install -r requirements.txt
      
-- mark "src" folder as Source Folder 

-- Create Run/Debug Configuration :

    - select src/social_network/__main__.py as script 
    
      - add environment variables :     
    
        PYTHONUNBUFFERED=1;
        DATABASE_URL=sqlite:///database.sqlite3;
        JWT_SECRET=42E1F6490772378C6BA2BF9C5692C20913DBD18EF25FB1E0D45EB6728D86671A;
        SERVER_HOST=127.0.0.1;
        SERVER_PORT=8000
        
-- Run created Configuration 

-- Check http://127.0.0.1:8000/docs

-- Sign_up 

-- Create posts

-- and check http://127.0.0.1:8000/ui/posts

-- create another user and create new posts with his credentials in /docs

-- and can create likes for previous posts with id number for each

FINISH !!
--------------------
