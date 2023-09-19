import { useQuery } from "react-query"

const BE_URL = 'http://127.0.0.1:5000'

export const useCvQuery = (cvId: string) => {
    const query = useQuery<any>(['cv', cvId],
        () => fetch(`${BE_URL}/cv/${cvId}`).then(res => res.json())
    )
    return query
}