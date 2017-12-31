import * as React from "react";
import Form from './Form'

interface IAppProps {
}

export class App extends React.Component<IAppProps, {}> {
    constructor(props) {
        super(props)
    }

    handleFormSubmit(input){
        console.log(input)
    }

    render() {
        return (
        <Form onSubmitForm={this.handleFormSubmit}/>
    )
    }
}