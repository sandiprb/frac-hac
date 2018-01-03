import * as React from 'react'
import './Button.css'

interface IButton {
	className?: string
	isLoading?: boolean
	title?: string
	onClick: Function
}

const Button = ({ className, isLoading, title, onClick }: IButton) => {
	return (
		<button className={`button ${className}`} disabled={isLoading} onClick={() => onClick()}>
			{isLoading ? (
				<div className="spinner">
					<div className="bounce1" />
					<div className="bounce2" />
					<div className="bounce3" />
				</div>
			) : (
				title
			)}
		</button>
	)
}

export default Button
