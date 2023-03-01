import redis, {createClient} from 'redis';

const client = createClient();

client.on('error', (err)=> console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const subscriber = client.duplicate();

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    if (channel === 'holberton school channel') console.log(message);
    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe(channel);
      subscriber.quit();
    }
});