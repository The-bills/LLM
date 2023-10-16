import { FileDrop } from "../../components/FileDrop"
import { PageWithNavbar } from "../../layouts/PageWIthNavbar"
import { useTokenCountQuery } from "../../queries/useTokenCountQuery"

export const Home = () => {
    const tokens = useTokenCountQuery()
    return (
        <PageWithNavbar>
            <h1 className='text-3xl font-bold mb-8'>Home</h1>
            {tokens.embedding} - 
            {tokens.llm}
            <FileDrop />
        </PageWithNavbar>
    )
}