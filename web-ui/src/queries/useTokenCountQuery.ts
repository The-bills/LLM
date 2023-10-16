import { useQuery } from "react-query"
import { Position } from "../types/position"

const BE_URL = 'http://127.0.0.1:5000'

export const useTokenCountQuery = () => {
    const query_embedding = useQuery<number>('tokens_embedding',
        () => fetch(`${BE_URL}/tokens/embedding`).then(res => res.json())
    )
    const query_llm = useQuery<number>('tokens_llm',
        () => fetch(`${BE_URL}/tokens/llm`).then(res => res.json())
    )
    return {
        isLoading: query_embedding.isLoading || query_llm.isLoading,
        llm: query_llm.data,
        embedding: query_embedding.data
    }
}