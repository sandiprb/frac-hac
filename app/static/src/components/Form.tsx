import * as React from "react";
import Button from './Buttons'

const PID_REGEX = /[A-Z0-9]{10}/g


interface IFormProps {
    onSubmitForm: (pid, query)=> void
    isLoading?:boolean
    isFormSubmitted: boolean
}

interface IFormState {
    searchText?: string
    errorMsg?: string
    isValid?: boolean
    query?: string
    pid?: string
}

export default class Form extends React.Component <IFormProps, IFormState> {
    private input: HTMLInputElement;

    static defaultProps = {
        isFormSubmitted: false
    }

    constructor(props){
        super(props)
        this.state = {
            searchText: "can I use 'B00028OSI0'on my face?",
            errorMsg: '',
            isValid: true
        }

    }

    componentDidMount() {
        this.input.focus()
    }

    private isValid = (cb:Function) => {
        const { searchText } = this.state

        let pid:string
        let query:string
        let isValid:boolean = true
        let errorMsg:string = ''

        if (!searchText.trim()){
            isValid = false
            errorMsg = "Please enter a query to search for!!"
        }else if (!PID_REGEX.test(searchText)){
            isValid = false
            errorMsg = "Please enter a valid Asin in query!"
        }else {
            const matchedPID = searchText.match(PID_REGEX)
            pid = matchedPID[0]
            query = searchText.replace(pid, "").replace(/'/g, "")
            isValid = true
        }
        this.setState({isValid, errorMsg, pid, query}, ()=> {
            isValid && cb && cb()
        })
    }

    handleInputChange(e) {
        this.setState({searchText: e.target.value})
    }

    handleSubmitForm = () => {
        this.isValid(this.processForm)
    }

    processForm = () => {
        const {pid, query} = this.state
        this.props.onSubmitForm(pid, query)
    }

    render() {
        const {isFormSubmitted} = this.props
        const {searchText, errorMsg} = this.state
        return (
            <div className={`form-wrapper ${isFormSubmitted ? 'submitted': ''}`}>
                <h2 className="text-center">Welcome! </h2>
                <div className="form-group">
                    <input ref={(input) => { this.input = input }} value={searchText} placeholder='Search for query!' className='form-control' onChange={(e) => this.handleInputChange(e)} />
                    {errorMsg && <div className="text-error">{errorMsg}</div>}
                </div>

                    <Button className="button button-purple" isLoading={this.props.isLoading} onClick={this.handleSubmitForm.bind(this)} title='Search'/>
            </div>
        )
    }
}