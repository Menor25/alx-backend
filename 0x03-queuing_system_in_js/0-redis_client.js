import { createClient } from 'redis';

// create a Redis client instance
const client = createClient();

// log any errors that occur while connecting to the Redis server
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

// log a message when successfully connect to the server
client.on('connect', () => {console.log('Redis client connected to the server')});