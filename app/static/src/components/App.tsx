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
}

export class App extends React.Component<IAppProps, IAppState> {
	state: IAppState

	constructor(props: IAppProps) {
		super(props)
		this.state = {
			isLoading: false,
			isFormSubmitted: false,
			isAnswerFetched: false,
		}
	}

	private getAnswer = async (pid, query) => {
		const { data: answer, success: apiSuccess, error: apiError = '' } = await APIfetchAnswer(pid, query)
		const newState = {
			isLoading: false,
			isAnswerFetched: true,
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

	render() {
		const { isLoading, isAnswerFetched, isFormSubmitted, answer, anwerApiResponse } = this.state

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
					</section>
				)}
			</div>
		)
	}
}
