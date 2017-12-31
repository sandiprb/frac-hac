import * as React from "react";
import ContentLoader from "react-content-loader"

import { IAnswer } from '../interface'


const AnswerLoader = () => (
	<ContentLoader
		height={200}
		width={505}
		speed={2}
		primaryColor={"#f3f3f3"}
		secondaryColor={"#ecebeb"}
	>
		<rect x="25" y="15" rx="5" ry="5" width="680" height="10" />
		<rect x="25" y="45" rx="5" ry="5" width="400" height="10" />
		<rect x="585" y="-45" rx="5" ry="5" width="420" height="10" />
		<rect x="141" y="71" rx="5" ry="5" width="100" height="10" />
		<rect x="26" y="72" rx="5" ry="5" width="100" height="10" />
	</ContentLoader>
)

interface IProps {
    answer: IAnswer
    isFetching: boolean
}

export const AnswerCard = ({isFetching, answer}: IProps) => {
    return (
            <div className="answer-wrapper">

                {answer && <p>Based on your query, we Found following question!</p>}
                <div className="answer-card">

                {
                isFetching ?
                    <AnswerLoader />
                 :
                 <div>
                    <h5>{answer.question}</h5>
                    <h6 style={{opacity: 0.7}}>{answer.answer}</h6>
                    <hr/>
                    <div className="answer-card__footer">
                        {answer.asin && <div> <span className='key'> Asin: </span> {answer.asin} </div>}
                        {answer.answerTime && <div><span className='key'> Answer Time: </span> {answer.answerTime} </div>}
                        {answer.questionType && <div> <span className='key'> Question Type:</span>{answer.questionType} </div>}
                    </div>
                 </div>
                }
                </div>
            </div>


    )
}