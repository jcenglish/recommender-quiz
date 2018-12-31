import React from 'react'
import {connect} from 'react-redux'
import {Login} from './'
/**
 * COMPONENT
 */
export const UserHome = props => {
  return (
    <div>
      <Login />
    </div>
  )
}

/**
 * CONTAINER
 */
// const mapState = state => {
//   return {
//     email: state.user.email
//   }
// }

export default UserHome
