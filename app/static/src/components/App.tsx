import * as React from "react";
import Form from './Form'

import {fetchAnswer} from '../api'

type IAnswer = {
    answer: string
    answerType: string
    asing: string
    id: string
    question: string
    questionType: string
    answerTime?: string
    unixTime?: number
}

interface IAppProps {
}

interface IAppState {
    answer?: IAnswer
    isLoading: boolean
}

export class App extends React.Component<IAppProps, IAppState> {
    state: IAppState

    constructor(props: IAppProps) {
        super(props)
        this.state = {
            isLoading: false
        }
    }

    private getAnswer = async(input) => {
        let answerData = await fetchAnswer(input)
        answerData = answerData as IAnswer
        answerData && this.setState({ answer : answerData, isLoading: false})
    }

    handleFormSubmit = (input) => {
        this.setState({isLoading: true})
        this.getAnswer(input)
    }

    render() {
        const { isLoading } = this.state
        return (
        <Form onSubmitForm={this.handleFormSubmit} isLoading={isLoading}/>
    )
    }
}