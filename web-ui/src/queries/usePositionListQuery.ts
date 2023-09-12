import { useQuery } from "react-query"

const BE_URL = 'http://127.0.0.1:5000'

export const usePositionListQuery = () => {
    const query = useQuery<any[]>('positionList', () => fetch(`${BE_URL}/positions`).then(res => res.json()))
    return query
}