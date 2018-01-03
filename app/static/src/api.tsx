const error = 'Oops! Something blew up.. Please try again later.'

const fetchAPI = async data => {
	try {
		const response = await fetch('/api/', {
			method: 'post',
			body: JSON.stringify(data),
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
		})
		const { status } = response
		if (status == 200) {
			let result = await response.text()
			result = result.replace(/\bNaN\b/g, null)
			return JSON.parse(result)
		} else {
			return { error }
		}
	} catch (e) {
		console.log(e)
		return { error }
	}
}

export const fetchAnswer = async (pid: string, query: string) => {
	const queryData = { pid, query }
	const result = await fetchAPI(queryData)
	return result
}
