const mqtt = require('mqtt')
const clientId = `mqtt_${Math.random().toString(16).slice(3)}`

const connectUrl = `wss://vernemq-testops.pwc.dev.cos.pwtestops.com/mqtt`
const client = mqtt.connect(connectUrl, {
  clientId,
  clean: true,
  connectTimeout: 4000,
  username: 'tsmmqttuser',
  password: 'ZFjN39bfg4YgCL9d',
  reconnectPeriod: 1000,
  rejectUnauthorized: false
})

const topic = '/nodejs/mqtt'
client.on('connect', () => {
  console.log('Connected')
  client.subscribe([topic], () => {
    console.log(`Subscribe to topic '${topic}'`)
  })
})
client.on('message', (topic, payload) => {
  console.log('Received Message:', topic, payload.toString())
  process.exit();
})
