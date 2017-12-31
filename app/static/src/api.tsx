const SITE_DOMAIN = window['URL'] || 'http://127.0.0.1:5000/'
const API_URL = `${SITE_DOMAIN}api/`

const fetchAPI = async(data) => {
    try {
        const response = await fetch('/api/', {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        })
        const result = await response.json()
        return result
    } catch (error) {
        throw error
    }
}

export const fetchAnswer = async(query: string) => {
    const queryData = {
        query
    }
    const result = await fetchAPI(queryData)
    const { data } = result
    return data[0]
}
