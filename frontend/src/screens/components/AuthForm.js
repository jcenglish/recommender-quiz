import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import {connect} from 'react-redux'
import {auth, clearError} from '../../store'

class AuthForm extends Component {
  render() {
    let {name, displayName, handleSubmit, error} = this.props

    return (
      <div>
        <div>
          <h2>{name === 'login' ? 'Log in' : 'Create an account'}</h2>
          <h3>
            or{' '}
            {name === 'login' ? (
              <Link to="/signup" onClick={() => this.props.removingError()}>
                create an account
              </Link>
            ) : (
              <Link to="/" onClick={() => this.props.removingError()}>
                log in
              </Link>
            )}
          </h3>
        </div>
        <form autoComplete="off" onSubmit={handleSubmit} name={name}>
          <input
            required
            label="Email"
            type="email"
            name="email"
            autoComplete="email"
          />
          <input
            required
            label="Password"
            type="password"
            name="password"
            autoComplete="current-password"
          />
          <button type="submit" name="">
            {displayName}
          </button>
        </form>
        <span>
          {error && error.response && <div> {error.response.data} </div>}
        </span>
      </div>
    )
  }
}

const mapLogin = state => {
  return {
    name: 'login',
    displayName: 'Login',
    error: state.user.error
  }
}

const mapSignup = state => {
  return {
    name: 'signup',
    displayName: 'Sign Up',
    error: state.user.error
  }
}

const mapDispatch = dispatch => {
  return {
    handleSubmit: evt => {
      evt.preventDefault()
      const formName = evt.target.name
      const email = evt.target.email.value
      const password = evt.target.password.value
      dispatch(auth(email, password, formName))
    },
    removingError: () => {
      dispatch(clearError())
    }
  }
}

export const Login = connect(
  mapLogin,
  mapDispatch
)(AuthForm)

export const Signup = connect(
  mapSignup,
  mapDispatch
)(AuthForm)
