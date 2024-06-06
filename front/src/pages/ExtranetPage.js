
import { Link, Outlet } from "react-router-dom";
import Header from "../components/header";
import styles from './pages.module.css'


export default function ExtranetPage() {
    return (
        <div className={styles.base_page}>
            <Header />
            <div>
                <Outlet />
            </div>
        </div>
    );

}