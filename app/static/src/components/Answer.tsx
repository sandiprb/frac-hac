import * as React from 'react'

import { IAnswer } from '../interface'

interface IProps {
	answer: IAnswer
}

export const AnswerCard = ({ answer }: IProps) => {
	return (
		<section className="section">
			<div className="answer-wrapper unit-appear-up">
				<div className="answer-card">
					<div>
						<h5>{answer.question}</h5>
						<h6 style={{ opacity: 0.7 }}>{answer.answer}</h6>
						<hr />
						<div className="answer-card__footer">
							{answer.asin && (
								<div>
									{' '}
									<span className="key"> Asin: </span> {answer.asin}{' '}
								</div>
							)}
							{answer.answerTime && (
								<div>
									<span className="key"> Answer Time: </span> {answer.answerTime}{' '}
								</div>
							)}
						</div>
					</div>
				</div>
			</div>
		</section>
	)
}
