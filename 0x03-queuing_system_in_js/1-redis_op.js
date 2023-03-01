import { createClient } from 'redis';

// create a Redis client instance
const client = createClient();

// log any errors that occur while connecting to the Redis server
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

// log a message when successfully connect to the server
client.on('connect', () => {console.log('Redis client connected to the server')});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, resp) => {
        if(err) console.log(err);
        redis.print(resp);
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, resp) => {
        if(err) console.log(err);
        redis.print(resp);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');