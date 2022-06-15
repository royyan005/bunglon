import os
with open(os.path.join('./','Procfile'), "w") as file1:
    toFile = 'worker: sh setup.sh && echo PORT $PORT && streamlit run  --server.port $PORT main.py'
    
file1.write(toFile)