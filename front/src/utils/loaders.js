import { request_sender } from "../components/functions";

export function companies_loader({params}){
    let companies =   request_sender
    .get("/distributing/extranet/" + params.id + '/company')
    .then( (response) => {
        console.log(response)
        return response.data
    })
    return companies
 
}