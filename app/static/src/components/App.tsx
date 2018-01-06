import * as React from 'react'
import Form from './Form'
import { AnswerCard } from './Answer'

import { fetchAnswer as APIfetchAnswer } from '../api'
import { IAnswer } from '../interface'

interface IAppProps {}

interface IAppState {
	answer?: IAnswer
	isLoading: boolean
	isAnswerFetched: boolean
	isFormSubmitted: boolean
	anwerApiResponse?: string
	reviews?: any
}

export class App extends React.Component<IAppProps, IAppState> {
	state: IAppState

	constructor(props: IAppProps) {
		super(props)
		this.state = {
			isLoading: false,
			isFormSubmitted: false,
			isAnswerFetched: false,
			reviews: [],
		}
	}

	private getAnswer = async (pid, query) => {
		const { data: answer, success: apiSuccess, error: apiError = 'No data found', reviews = [] } = await APIfetchAnswer(
			pid,
			query
		)
		const newState = {
			isLoading: false,
			isAnswerFetched: true,
			reviews,
		}
		if (!apiSuccess) {
			this.setState({
				anwerApiResponse: apiError,
				isFormSubmitted: false,
				...newState,
			})
			return
		}
		answer &&
			this.setState({
				answer,
				...newState,
			})
	}

	handleFormSubmit = (pid, query) => {
		this.setState({
			isLoading: true,
			isFormSubmitted: true,
		})
		this.getAnswer(pid, query)
	}

	handleNewSearch = () => {
		this.setState({
			isFormSubmitted: false,
			isLoading: false,
			isAnswerFetched: false,
			answer: null,
		})
	}

	getReviewsJSX = () => {
		const {reviews} = this.state
	}

	render() {
		const { isLoading, isAnswerFetched, isFormSubmitted, answer, anwerApiResponse, reviews } = this.state
		const reviewMojis = {
			'0': '😑',
			'1':'😄',
			'-1':'😟',
		}

		const reviewsJSX = reviews.length && reviews.map((v, i) => {
return (
			<div className="card" key={i} style={{marginTop: 12}}>
						<div className="card bg-light3">
							<div className="card-header">


							<div className="pull-right">
								BM25 Score: {parseFloat(v.bm25_score).toFixed(2)}

							</div>
								<div>

								Sentiment:
								{reviewMojis[v.sentiment_type]}
								</div>
							</div>

							<div className="card-body">
								<h4 className="card-title"> {v.summary} </h4>
								<p className="card-text">{v.reviewText}</p>
							</div>
						</div>
					</div>
					)
				})

		return (
			<div>
				<Form onSubmitForm={this.handleFormSubmit} isFormSubmitted={isFormSubmitted} isLoading={isLoading} />
				{isAnswerFetched && (
					<section className="section">
						{answer ? (
							<div>
								<p>We found a related answer!</p>
								<AnswerCard answer={answer} />
								<div className="text-right">
									<button className="btn btn-link" onClick={this.handleNewSearch}>
										Search for another query?
									</button>
								</div>
							</div>
						) : (
							<div className="alert alert-danger">{anwerApiResponse}</div>
						)}
						{reviews.length ?
						<div>
							<h4>Matched Reviews for the product: </h4>
							{reviewsJSX}
						</div>
						: null}
					</section>
				)}


			</div>
		)
	}
}
