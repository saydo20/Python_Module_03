import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            scores = []
            i = 1
            while i < len(sys.argv):
                if int(sys.argv[i]) < 0:
                    raise ValueError("the score must be positive")
                scores = scores + [int(sys.argv[i])]
                i += 1
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")
        except ValueError as error:
            print(f"invalid scores : {error}")
        except Exception as Error:
            print(f"Unexpected error: {Error}")


def main() -> None:
    try:
        score_analytics()
    except Exception as error:
        print(f"error : {error}")


main()
