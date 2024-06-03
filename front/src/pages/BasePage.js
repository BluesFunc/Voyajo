import { Outlet } from 'react-router-dom';

import Header from '../components/header'
import styles from './pages.module.css'


export default function BasePage() {
    return (
        <div  className={styles.base_page}>
            <Header/>
            <Outlet/>
        </div>
    );
}