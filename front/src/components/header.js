import { Link } from "react-router-dom"
import styles from './components.module.css'
import { useState } from "react";

import logout from "./functions";



export default function Header() {
    const user_token = localStorage.getItem("UserToken")



    return (
        <nav className={styles.main_header}>
            <Link to="/">Главная</Link>
            <Link>Избранное</Link>
            {
                user_token 
                ? (
                    <div className={styles.logout_block}>
                    <Link to="/">{user_token}</Link>
                    <button onClick={logout}>Выйти</button>
                    </div>
                ) 
                : (<Link to="/login">Войти</Link>)    

            }
        </nav>
    );


}