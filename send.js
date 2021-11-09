const amqp = require('amqplib/callback_api')
const logger = require('./utils/logger')
require('dotenv').config()

amqp.connect(process.env.CLOUDAMQP_URL, (error0, connection) => {
    if (error0) {
        logger.error(error0)
    }

    connection.createChannel((error1, channel) => {
        if (error1) {
            logger.error(error1)
        }
        const queue = 'wikiscrape-zach'

        channel.assertQueue(queue, {
            durable: false
        }, (error2) => {        // callback after assert
            if (error2) {
                logger.error(error2)
            }

            const correlationId = generateUUid()
            const send_msg = {
                "query": "pomeranian_dog"
            }

            logger.info('requesting')

            channel.consume(queue, (msg) => {
                if (msg.properties.correlationId == correlationId) {
                    logger.info(`Got ${msg.content.toString()}`)
                    setTimeout(() => {
                        connection.close()
                        process.exit(0)
                    }, 500)
                }
            }, {
                noAck: true
            })

            channel.sendToQueue('wikiscrape',
                Buffer.from(JSON.stringify(send_msg)), {
                    contentType: 'application/json',
                    correlationId: correlationId,
                    replyTo: queue
                })
        })
    })
})

const generateUUid = () => {
    return Math.random().toString() +
        Math.random().toString() +
        Math.random().toString()
}