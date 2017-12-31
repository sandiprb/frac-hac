import * as React from "react";
import Button from './Buttons'

interface IFormProps {
    onSubmitForm: (input)=> void
    isLoading?:boolean
}

interface IFormState {
    searchText?: string
}


export default class Form extends React.Component <IFormProps, IFormState> {
    private input: HTMLInputElement;

    constructor(props){
        super(props)
        this.state = {
            searchText: "smooth 602260074X"
        }
    }

    componentDidMount() {
        this.input.focus()
    }

    handleInputChange(e) {
        this.setState({searchText: e.target.value})
    }

    handleSubmitForm = () => {
        this.props.onSubmitForm(this.state.searchText)
    }

    render() {
        return (
            <div className='form-wrapper'>
                <h2 className="text-center">Welcome! </h2>
                <div className="form-group">
                    <input ref={(input) => { this.input = input }} value={this.state.searchText} placeholder='Search for query!' className='form-control' onChange={(e) => this.handleInputChange(e)} />
                </div>

                    <Button className="button button-purple" isLoading={this.props.isLoading} onClick={this.handleSubmitForm.bind(this)} title='Search'/>
            </div>
        )
    }
}