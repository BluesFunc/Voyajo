import { Link, useLoaderData } from "react-router-dom";
import styles from './components.module.css'


export default function Company_block() {
  const companies = useLoaderData()
  console.log(companies)
  return (
    
    <div style={{"boxSizing": "border-box"}} >
    <Link to='company/add' style={{'margin': '50px'}}> Добавить компанию</Link>   
    <br></br>

    <ul>
      {companies.map((company) => (
        <li id={company.id}>
        <div className={styles.content_block}>
          <span>
            <strong>Company Name:</strong> {company.name}
          </span>
          <span>
          </span>
          <span>
            <strong>Company Type:</strong> {company.company_type}
          </span>
          <span>
            <strong>Company Link:</strong> <a href={company.company_link} target="_blank" rel="noopener noreferrer">Перейти</a>
          </span>
        </div>
        </li>
        
      ))}
      </ul>
      </div>
  )
}