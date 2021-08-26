db.auth('adminuser', 'adminpassword')

db = db.getSiblingDB('testdb')

db.createUser(
        {
            user: "testuser",
            pwd: "test1234",
            roles: [
                {
                    role: "readWrite",
                    db: "testdb"
                }
            ]
        }
);