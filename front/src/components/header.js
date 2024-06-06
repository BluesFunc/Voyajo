import { Link } from "react-router-dom"
import styles from './components.module.css'
import { useState } from "react";

import logout from "./functions";



export default function Header() {
    const user = localStorage.getItem("User")
    const role = localStorage.getItem("UserRole")
    const role_id = localStorage.getItem('RoleID')

    return (
        <div className={styles.main_header}>
            <Link to="/">Главная</Link>
            {role == 'customer' && <Link to='/tickets'>Билеты</Link>}
            {
                user 
                ? (
                    <div className={styles.logout_block}>
                    <Link to={'/' + role + '/' + role_id}>{user}</Link>
                    <button onClick={logout}>Выйти</button>
                    </div>
                ) 
                : (<Link to="/login">Войти</Link>)    

            }
        </div>
    );


}