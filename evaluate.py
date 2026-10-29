from src.retriever import RAGSystem


GOLDEN_SET = [
    {
        "pregunta": "¿Qué código HTTP indica que se creó un recurso?",
        "documento_id_esperado": "http_status.md",
    },
    {
        "pregunta": "¿Qué método de Python agrega un elemento al final de una lista?",
        "documento_id_esperado": "python_listas.md",
    },
    {
        "pregunta": "¿Qué es una API REST y qué métodos HTTP utiliza?",
        "documento_id_esperado": "apis_rest.md",
    },
    {
        "pregunta": "¿Para qué sirve una clave primaria en SQL?",
        "documento_id_esperado": "sql_bases_datos.md",
    },
    {
        "pregunta": "¿Qué diferencia hay entre git commit y git push?",
        "documento_id_esperado": "git_control_versiones.md",
    },
]


def main():
    system = RAGSystem(k=5)

    precision_scores = []
    recall_scores = []

    print("\nEVALUACIÓN DEL RECUPERADOR HÍBRIDO")
    print("=" * 45)

    for case in GOLDEN_SET:
        results = system.retrieve(case["pregunta"])
        expected = case["documento_id_esperado"]

        relevant = [
            document
            for document in results
            if document.metadata.get("source") == expected
        ]

        precision = len(relevant) / 5
        recall = 1.0 if relevant else 0.0

        precision_scores.append(precision)
        recall_scores.append(recall)

        sources = [
            document.metadata.get("source", "Sin fuente")
            for document in results
        ]

        print(f"\nPregunta: {case['pregunta']}")
        print(f"Documento esperado: {expected}")
        print(f"Fuentes recuperadas: {sources}")
        print(f"Precision@5: {precision:.2%}")
        print(f"Recall@5: {recall:.2%}")

    print("\n" + "=" * 45)
    print(
        "Precision@5 promedio: "
        f"{sum(precision_scores) / len(precision_scores):.2%}"
    )
    print(
        "Recall@5 promedio:    "
        f"{sum(recall_scores) / len(recall_scores):.2%}"
    )
    print(
        "\nRelevancia definida por coincidencia entre "
        "el archivo fuente recuperado y el esperado."
    )


if __name__ == "__main__":
    main()
