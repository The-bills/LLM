import { useQuery } from "react-query"
import { Position } from "../types/position"

const BE_URL = 'http://127.0.0.1:5000'

export const usePositionQuery = (positionId: string) => {
    const query = useQuery<Position>(['position', positionId],
        () => fetch(`${BE_URL}/positions/${positionId}`).then(res => res.json())
    )
    return query
}