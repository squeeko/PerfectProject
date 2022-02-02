from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.on_event("startup")
async def startup_event():
    return {"message": "Startup Successful!"}

@app.on_event("shutdown")
async def shutdown_event():
    with open("log.txt", mode='a') as log:
        log.write("Application Shutdown")
        
# I will use the asgi-lifetime function for startup and shutdown events soon. 