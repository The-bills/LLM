import { useQuery } from "react-query"

const BE_URL = 'http://127.0.0.1:5000'

export const useCvListQuery = () => {
    const query = useQuery<any[]>('cvList', () => fetch(`${BE_URL}/cv`).then(res => res.json()))
    return query
}