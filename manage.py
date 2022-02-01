from app import create_app


# Creating app instance
app = create_app('development')

# Creating app instance


#manager.add_command('server',Server)

if __name__ == '__main__':
    app.run()