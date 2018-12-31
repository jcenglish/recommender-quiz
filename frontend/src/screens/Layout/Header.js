import React from 'react'
import {connect} from 'react-redux'
import {LayoutNav} from './'
/**
 * COMPONENT
 */
export const LayoutHeader = props => {
  return (
    <header>
      <LayoutNav />
    </header>
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

export default LayoutHeader
