

from datetime import datetime


def create_report(
    candidate_name,
    result
):

    report = []

    report.append("=" * 70)

    report.append(
        "AI-POWERED INTERVIEW QUESTION GENERATOR"
    )

    report.append("=" * 70)

    report.append("")

    report.append(
        f"Candidate: {candidate_name}"
    )

    report.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

    report.append("")

    report.append(
        result
    )

    return "\n".join(report)


def save_report(
    report,
    output_path
):

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        f"Report saved to: {output_path}"
    )