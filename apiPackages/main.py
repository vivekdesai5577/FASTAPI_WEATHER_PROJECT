import uvicorn
from fastapi import FastAPI
from apiPackages.routes import create_new_user, read_users, read_user_by_name, weather_city
# from apiPackages.routes import router

app = FastAPI()

##Define all route configurations
def configuration():

    ##Route configuration for all APIS
    app.include_router(create_new_user.router) #, prefix="/apiPackages/routes/create_new_user")
    app.include_router(read_users.router) #, prefix="/apiPackages/routes/read_users")
    app.include_router(read_user_by_name.router) #, prefix="/apiPackages/routes/read_user_by_name")
    app.include_router(weather_city.router) #, prefix="/apiPackages/routes/weather_city")
    #app.include_router(autentication.router) #, prefix="/apiPackages/routes/weather_city")
    # app.include_router(router, prefix="/apiPackages/routes")

##Call all route configuration
configuration()

if __name__ == '__main__':

    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
