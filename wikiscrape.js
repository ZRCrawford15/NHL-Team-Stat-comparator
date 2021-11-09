const axios = require('axios')
const cheerio = require('cheerio')

const getImage = async (query) => {
    console.log(query);
    const response = await axios.get(`https://en.wikipedia.org/wiki/${query}`)
    const html = cheerio.load(response.data)
    const imageUrl = html('td[class=infobox-image]').children('a').children('img').attr('src')
    return 'https:' + imageUrl
}

module.exports =  {getImage}