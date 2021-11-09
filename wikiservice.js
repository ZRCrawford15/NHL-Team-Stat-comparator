const amqp = require('amqplib/callback_api')
const logger = require('./utils/logger')
require('dotenv').config()
const wikiservice = require('./wikiscrape')

amqp.connect('amqp://localhost', (error0, connection) => {
    if (error0) {
        logger.error(error0)
    }

    connection.createChannel((error1, channel) => {
        if (error1) {
            logger.error(error1)
        }

        const queue = 'wikiscrape'

        channel.assertQueue(queue, {
            durable: false
        })
        logger.info('awaiting RPC requests')
        channel.consume(queue, async (msg) => {
            const image_query = JSON.parse(msg.content).query

            // get image
            const image_url = await wikiservice.getImage(image_query)

            const payload = {"image_url": image_url}
            logger.info(JSON.stringify(payload))

            channel.sendToQueue(msg.properties.replyTo,
                Buffer.from(JSON.stringify(payload)), {
                    correlationId: msg.properties.correlationId
                })

            channel.ack(msg)
        })
    })
})
