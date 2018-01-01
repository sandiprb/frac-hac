import * as React from "react";
import Form from './Form'
import { AnswerCard } from "./Answer";

import { fetchAnswer } from '../api'
import { IAnswer } from '../interface'

interface IAppProps {
}

interface IAppState {
    answer?: IAnswer
    isLoading: boolean
    isAnswerFetched: boolean
    isFormSubmitted: boolean
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

    private getAnswer = async(input) => {
        let answerData = await fetchAnswer(input)
        answerData = answerData as IAnswer
        answerData && this.setState({
            answer : answerData,
            isLoading: false,
            isAnswerFetched: true,
        })
    }

    handleFormSubmit = (input) => {
        this.setState({
            isLoading: true,
            isFormSubmitted: true,
        })
        this.getAnswer(input)
    }

    handleNewSearch = () => {
        this.setState({
            isFormSubmitted: false,
            isLoading: false,
            isAnswerFetched: false,
            answer: null
        })
    }

    render() {
        const { isLoading, isAnswerFetched, answer, isFormSubmitted } = this.state
        return (
            <div>
                <Form onSubmitForm={this.handleFormSubmit} isFormSubmitted={isFormSubmitted} isLoading={isLoading}/>
                {isAnswerFetched && <AnswerCard isFetching={isLoading} answer={answer} />}
                {isAnswerFetched &&
                <div className="text-right">
                    <button className="btn btn-link" onClick={this.handleNewSearch}>Search for another query?</button>
                </div>
                }
            </div>
    )
    }
}