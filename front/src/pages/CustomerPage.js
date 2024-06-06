
import LoginForm from "../components/login_form"
import styles from './pages.module.css'


export default function CustomerPage() {
    return (
        <div className={styles.login_page}>
            <LoginForm />
        </div>
    );

}